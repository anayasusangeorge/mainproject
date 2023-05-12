# from django.conf import settings
from django.urls import path

from interapp import views
# from django.conf.urls.static import static
#
# urlpatterns += static(settings.MEDIA_URL,
#                       document_root=settings.MEDIA_ROOT)

urlpatterns = [

    path('',views.index,name='index'),

    # path('LOGIN',views.LOGIN,name='LOGIN'),
    # path('REG',views.REG,name='REG'),
    path('login/',views.login,name='login'),
    path('register', views.register, name='register'),
    path('company', views.company, name='company'),
    path('students', views.students, name='students'),
    path('student_details/<int:id>/', views.student_details, name='student_details'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('courses/',views.courses,name='courses'),
    path('course-details/<int:id>/',views.course_details,name='course_details'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('pricing/',views.pricing,name='pricing'),
    path('logout/',views.logout,name='logout'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    # path('enroll_course/',views.enroll_course,name='enroll_course'),
    # path('endroll/<slug:course_slug>/',views.Course_endroll,name='endroll'),
    path('profile/',views.profile,name='profile'),
    path('searchbar/',views.searchbar,name='searchbar'),
    path('profile/update',views.profile_update,name='profile_update'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('paymentapproved/<str:leave_id>',views.paymentapproved,name='paymentapproved'),
    path('paymentdisapprove/<str:leave_id>', views.paymentdisapprove,name="paymentdisapprove"),
    path('admin/', views.admin, name='admin'),
    path('internship/', views.internship, name='internship'),
    path('subjects/', views.subjects, name='subjects'),
    path('add_subjects/', views.add_subjects, name='add_subjects'),
    # path('subject_details/<int:id>/', views.subject_details, name='subject_details'),
    path('add_video/', views.add_video, name='add_video'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),
    path('edit_course/<int:id>/', views.edit_course, name='edit_course'),
    path('view_course/<int:id>/', views.view_course, name='view_course'),
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),
    path('quiz_details/', views.quiz_details, name='quiz_details'),
    path('feedback/<int:id>/', views.feedback, name='feedback'),
    path('curriculum/<int:id>/', views.curriculum, name='curriculum'),
    path('video_detail/<int:id>/', views.video_detail, name='video_detail'),
    path('mark_video_completed/<int:id>/', views.mark_video_completed, name='mark_video_completed'),
    path('student_feedback_save/<int:id>/', views.student_feedback_save, name="student_feedback_save"),
    path('cart/', views.cart, name='cart'),
    # path('ress/', views.ress, name='ress'),
    path('addcart/<int:id>/', views.addcart, name='addcart'),
    path('de_cart/<int:id>/', views.de_cart, name='de_cart'),
    path('quiz/<int:id>/<int:week>/', views.quiz, name='quiz'),
    path('quiz/result/generate_certificate/<str:percent>/<str:course_name>/<str:user_name>/', views.generate_certificate, name='generate_certificate'),
    path('durations/', views.durations, name='durations'),
    # path('document_similarity/', views.document_similarity, name='document_similarity'),
    path('resumeparser/', views.resumeparser, name='resumeparser'),
    path('resdetails/', views.resdetails, name='resdetails'),
    path('resubmit/', views.resubmit, name='resubmit'),
    path('transcribe_video/<int:id>/', views.transcribe_video, name='transcribe_video'),
    path('certi/', views.certi, name='certi'),
    path('feedback_view', views.feedback_view, name='feedback_view'),

    # //////////////////////////////////////////////////////
    path('res', views.res, name='res'),
    # path('admin_index', views.admin_index, name='admin_index'),
    path('my_view', views.my_view, name='my_view'),
    path('resdetails', views.resdetails, name='resdetails'),
    path('resubmit', views.resubmit, name='resubmit'),
    path('manage_resumes', views.manage_resumes, name='manage_resumes'),
    path('resume_delete/<int:res_id>', views.resume_delete, name='resume_delete'),
    path('interdetail', views.interdetail, name='interdetail'),
    path('projectdetail', views.projectdetail, name='projectdetail'),
    path('achidetail', views.achidetail, name='achidetail'),
    path('certidetail', views.certidetail, name='certidetail'),




]