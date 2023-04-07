import subprocess

from docx.shared import Cm  # pip install python-docx
from docxtpl import DocxTemplate, InlineImage  # pip install docxtpl
from typing import List

from pydantic import BaseModel


class Requirements(BaseModel):
    education: str | None = None
    work_experience: str | None = None
    security_clearance: str | None = None
    competences: List[str] | None = None
    personal_qualities: List[str] | None = None
    languages: List[str] | None = None
    software_knowledge: List[str] | None = None


class JobPosition(BaseModel):
    supervision: List[str] | None = None
    objectives: List[str] | None = None
    organizational_chart: str | None = None
    responsibilities_percent: List[int] | None = None
    responsibilities: List[List[str]] | None = None
    communication_level: List[str] | None = None
    requirements: Requirements | None = None
    approved_by: str | None = None


class JobDescription(BaseModel):
    document_header: str | None = None
    job_title: str | None = None
    department: str | None = None
    job_position: JobPosition | None = None
    instruction_signature: str | None = None


def convert_to_pdf(doc, path):
    subprocess.call(['soffice',
                     # '--headless',
                     '--convert-to',
                     'pdf',
                     '--outdir',
                     path,
                     doc])


def make_docx(result_file_name: str, job: JobDescription, image_name: str):
    doc = DocxTemplate('exem.docx')
    placeholder_1 = InlineImage(doc, image_name, Cm(17))
    context = {
        "placeholder_1": placeholder_1,
        "job_title": job.job_title,
        "department": job.department,
        "supervision": "/ ".join(job.job_position.supervision),
        "objectives": num_list(job.job_position.objectives),
        "education": job.job_position.requirements.education,
        "work_experience": job.job_position.requirements.work_experience,
        "security_clearance": job.job_position.requirements.security_clearance,
        "competences": dot_list(job.job_position.requirements.competences),
        "personal_qualities": dot_list(job.job_position.requirements.personal_qualities),
        "languages": ", ".join(job.job_position.requirements.languages),
        "software_knowledge": dot_list(job.job_position.requirements.software_knowledge)
    }

    for i in range(len(job.job_position.responsibilities_percent)):
        context["p" + str(i + 1)] = str(job.job_position.responsibilities_percent[i]) + "%"

    for i in range(len(job.job_position.responsibilities)):
        context["ptext" + str(i + 1)] = job.job_position.responsibilities[i][0] + ":\n" + dot_list(
            job.job_position.responsibilities[i][1:])

    for i in range(len(job.job_position.communication_level)):
        context["com_level" + str(i + 1)] = job.job_position.communication_level[i]

    doc.render(context)
    # doc.replace_pic('Placeholder.png', image_name)

    doc.save(result_file_name)


def num_list(l: List[str]):
    string = ""
    for i in range(len(l)):
        string += str(i + 1) + ". " + l[i] + "\n"
    return string[:-1]


def dot_list(l: List[str]):
    string = ""
    for i in range(len(l)):
        string += "• " + l[i] + "\n"
    return string[:-1]


job = JobDescription()
job.job_title = "BOSSssss"
job.department = "Департамент кала"
job.job_position = JobPosition()
job.job_position.supervision = ["Первый заместитель директора", "второй заместитель", "третий зам зам"]
job.job_position.objectives = ["отжумания", "делать кофе", "спать"]
job.job_position.responsibilities_percent = [1, 69, 2, 2, 8]
job.job_position.responsibilities = [['Список домашних животных', 'кошка', 'собака', 'хомяк', 'попугай', 'рыбки'],
                                     ['Список животных, обитающих в лесу', 'лось', 'медведь', 'олень', 'росомаха'],
                                     ['Список морских животных', 'кит', 'акула', 'краб', 'кораллы'],
                                     ['Список диких котов', 'тигр', 'пума', 'жагуар', 'леопард'],
                                     ['Список рептилий', 'анаконда', 'ящерица', 'черепаха', 'кобра']]
job.job_position.requirements = Requirements()
job.job_position.requirements.education = "3 класса"
job.job_position.requirements.work_experience = "5 лет грузчиком"
job.job_position.requirements.competences = ["Основы выживания на улице",
                                             "Знание городских улиц и мест, где можно найти еду и пристройку на ночь",
                                             "Понимание базовых правил личной гигиены"]
job.job_position.requirements.personal_qualities = ["Способность собрать нужные вещи для выживания на улице",
                                                    "Умение воровать еду и вещи",
                                                    "Навыки охоты на грызунов и других животных для получения пищи"]
job.job_position.requirements.languages = ["Экзотикон", "Криптан", "Английский"]
job.job_position.requirements.software_knowledge = ['Pythlang', 'MontyScript', 'Serpy', 'NumpyC', 'Pytheas',
                                                    'HydraLang', 'Kolybelny', 'Squeezy']
job.job_position.communication_level = ["МАМА", "ПАПА", "Братья"]
job.job_position.requirements.security_clearance = "Знает все секреты"

make_docx('exem1.docx', job, 'boss1.png')
convert_to_pdf('exem1.docx', "out")
