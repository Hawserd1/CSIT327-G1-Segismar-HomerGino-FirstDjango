from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AccountFlowTests(TestCase):
    def test_signup_shows_success_message_on_login_page(self):
        response = self.client.post(
            reverse('signup'),
            {
                'username': 'newstudent',
                'email': 'student@example.com',
                'first_name': 'New',
                'last_name': 'Student',
                'role': 'STUDENT',
                'course': 'Science',
                'password1': 'N0tCommon#2468',
                'password2': 'N0tCommon#2468',
            },
            follow=True,
        )

        self.assertRedirects(response, reverse('login'))
        self.assertContains(response, 'Your account was created successfully. Please log in.')

    def test_profile_update_changes_only_profile_fields(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username='student',
            password='N0tCommon#2468',
            role=user_model.Role.STUDENT,
            course='Science',
        )
        self.client.force_login(user)

        response = self.client.post(
            reverse('profile'),
            {
                'first_name': 'Updated',
                'last_name': 'Student',
                'email': 'updated@example.com',
                'course': 'Mathematics',
            },
        )

        self.assertRedirects(response, reverse('profile'))
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'Updated')
        self.assertEqual(user.last_name, 'Student')
        self.assertEqual(user.email, 'updated@example.com')
        self.assertEqual(user.course, 'Mathematics')
        self.assertEqual(user.role, user_model.Role.STUDENT)

    def test_profile_requires_login(self):
        response = self.client.get(reverse('profile'))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('profile')}",
        )
