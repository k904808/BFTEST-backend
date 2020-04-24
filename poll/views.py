import json

from .models import (
    Question,
    Choice,
    Case,
    Stack,
    User,
    Response,
    Result
)

from django.views        import View
from django.http         import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

class QuestionView(View):
    def get(self, request, question_id):
        questions = (
            Question.
            objects.
            get(id = question_id)
        )

        choices = (
            Choice.
            objects.
            filter(question_id = questions.id).
            values()
        )

        question_data = {
            'id'        : questions.id,
            'question'  : questions.question,
            'image_url' : questions.image_url,
            'choice'    : [
                {
                    'id'     : choice["id"],
                    'choice' : choice["choice"],
                } for choice in choices ]
        }

        return JsonResponse({"question_data" : question_data}, status = 200)

class ResultView(View):
    def post(self, request):
        try:
            score      = json.loads(request.body)["answer"]
            p_type     = json.loads(request.body)["type"]
            user_name  = json.loads(request.body)["user"]
            browser    = request.META['HTTP_USER_AGENT']
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR')

            user = User(
                name       = user_name,
                browser    = browser,
                ip_address = ip_address
            )

            count_front = 0
            count_valid_question = 0
            for question_id, choice_id in score.items():
                Response(
                    user     = user,
                    question = question_id,
                    choice   = answer_id
                ).save()

                if Choice.objects.select_related('stack').get(id = choice_id).stack == 1:
                    count_front += 1

                if Choice.objects.select_related('stack').get(id = choice_id).stack != null:
                    count_valid_question += 1

            if count_front == count_valid_question/2:
                result  = Result.objects.get(stack = 3)
                dev_fit = Result.objects.get(stack = 3)

            elif count_front > count_valid_question/2:
                result  = Result.objects.get(case = p_type, stack = 1)
                dev_fit = Result.objects.get(case = p_type, stack = 2)

            else:
                result  = Result.objects.get(case = p_type, stack = 2)
                dev_fit = Result.objects.get(case = p_type, stack = 1)

            user.result_id = result
            user.save()

            user_result = {
                'name'        : result.name,
                'description' : result.description,
                'image_url'   : result.image_url,
                'audio_url'   : result.audio_url,
                'dev_fit'     : dev_fit.name
            }

            return JsonResponse({"result" : user_result}, status = 200)

        except KeyError:
            return JsonResponse({"error" : "INVALID_KEYS"}, status = 400)
