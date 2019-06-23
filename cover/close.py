from __future__ import print_function


class Galf(object):
    def __init__(self):
        self.first_name = 'Gerardo Agustin'
        self.last_name = 'Larreinegabe Ferreira'
        self.address = '497 Coronel Gracia \n Asuncion-Paraguay'
        self.cell_phone = '+595 981 282 485'
        self.e_mail = 'alarreine@gmail.com'

    @property
    def fname(self):
        return self.first_name

    @property
    def lname(self):
        return self.last_name

    @property
    def email(self):
        return self.e_mail

    @property
    def phone(self):
        return self.cell_phone

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name


def header(personal_data):
    from datetime import date
    head = [
            personal_data.full_name,
            personal_data.phone,
            personal_data.email,
            '\n\n',
            date.today().strftime('%B %d, %Y'),
            '\n\n'
            ]
    return head


def opening():
    par = [
            'Dear Hiring Manager,\n\n',
            '\tI\'m writing to you to express my interest in the position of Software Engineer-Backend (100% Remote).',
            '\tWith 7 years of experience in this exciting world, moving from DBA, Java and Python developer and the',
            'last one as a DevOps Engineer showing that I\'m curious and open to learn and discover new things. I have',
            'also a Master degree in Software Engineer and other courses that you could read in my CV.',
            '\tI enjoy being challenged and work in a team, I think it is the best way to share and learn new',
            'techniques, aptitudes and to accomplish common goals.'
            ]
    return par


def body():
    par = [
            '\tIn my last experience as a DevOps Engineer, I was working in an agile team developing on Python. I have ',
            'been able to improve my skills in designing, debugging and optimizing code in a collaborative way. I',
            'know that my previous experience with Python it was not for a back-end implementation but in another hand',
            'I have worked with Java in different projects including back-end implementations.',
            '\tI found good reviews about Close and I would like to participate and collaborate on your project. I ',
            'think I would help you to achieve your goal and learn more about teamwork and Python.'
           ]

    return par


def closing(personal_data):
    par = [
            '\tYou can find on my CV that details my experience in software development. I can be reached anytime via',
            'my cell phone {0} or via email at {1}'.format(personal_data.phone, personal_data.email),
            '\tThank you for your time and consideration. I look forward to speaking with you about this opportunity.',
            '\nSincerely,\n\n{0}'.format(personal_data.full_name)
            ]

    return par


if __name__ == '__main__':
    '''My Awesome cover letter'''
    my_info = Galf()
    for line in header(my_info):
        print(line.rjust(120))

    cover_letter = opening() + body() + closing(my_info)
    for line in cover_letter:
        print(line.ljust(120))