import datetime
from enum import Enum
from abc import ABC, abstractmethod, abstractproperty # type: ignore
from typing import Optional 


class EmergencyContactLevel(Enum):
    PRIMARY = 1
    SECONDARY = 2


class EducationLevel(Enum):
    HIGH_SCHOOL = "High School Diploma"
    ASSOCIATE = "Associate's Degree"
    BACHELOR = "Bachelor's Degree"
    MASTER = "Master's Degree"
    PHD = "PhD/ Doctorate Degree"


class ApplicationBase(ABC):
    """abstract class to pass on abstract methods to the child class"""
    @abstractmethod
    def add_personal_info(self, full_name: str, date_of_birth: str, sex: str, home_address: str, phone_number_home: str, phone_number_mobile: str, email_address: str) -> None:
        pass
    
    @abstractmethod
    def add_language(self, lang: str, read_ability: str, write_ability: str, speak_ability: str) -> None:
        pass

    @abstractmethod
    def add_education(self, level: EducationLevel, university_name: str, university_location: str, university_country: str, attended_from: str, attended_to: str, certificates: str, main_field_of_study: str) -> None:
        pass

    @abstractmethod
    def add_work_experience(self, company: str, location: str, emp_from: str, emp_to: str, position: str, reason: str) -> None:
        pass


class InputFormatter(ABC):
    """abstract class to format US phone numbers"""

    def phoneNumberFormatter(self, num: str) -> int:
        formatted_number: str = ""
        # checking if the entered value begins with a 001...
        if num[0] == "0":
            formatted_number = num[3:]
        # checking if the entered value begins with a +1...
        elif num[0] == "+":
            formatted_number = num[2:]
        else:
            formatted_number = num
        # returning the value in int so that it will be stored as such
        if formatted_number.isdigit() and len(formatted_number) == 10:
            return int(formatted_number)
        else:
            raise ValueError("ValueError: Invalid Phone Number Input Provided!")
        
    def emailFormatChecker(self, email: str) -> str:
        if "@" in list(email):
            return email
        else:
            raise ValueError("ValueError: Invalid Email Input Provided!")
    
    def dateFormatter(self, date: str) -> datetime.date:
        from_parts = date.split('-')
        if len(from_parts) != 3:
            raise ValueError(f"ValueError.{__class__}: Date string must be in the format 'YYYY-MM-DD'.")
        try:
            # Convert each part to an integer and construct a date object
            year = int(from_parts[0])
            month = int(from_parts[1])
            day = int(from_parts[2])
            return datetime.date(year, month, day)
        except ValueError:
            # Raised if any part cannot be converted to an integer or if the date is invalid
            raise ValueError(f"ValueError.{__class__}: Invalid Date Input Provided!")


class PersonalInfo(InputFormatter):
    def __init__(self, full_name: str, date_of_birth: str, sex: str, home_address: str, phone_number_home: str, phone_number_mobile: str, email_address: str) -> None:
        self.__full_name = full_name
        self.__date_of_birth: datetime.date = self.dateFormatter(date_of_birth)
        self.__phone_number_home = self.phoneNumberFormatter(phone_number_home)
        self.__phone_number_mobile = self.phoneNumberFormatter(phone_number_mobile)
        self.__sex = sex
        self.__home_address = home_address
        self.__email_address = self.emailFormatChecker(email_address)
        self.__emergency_contact_primary = None
        self.__emergency_contact_secondary = None

    @property 
    def full_name(self) -> str:
        return self.__full_name
    @property
    def date_of_birth(self) -> datetime.date:
        return self.__date_of_birth
    @property
    def sex(self) -> str:
        return self.__sex
    @property 
    def home_address(self) -> str:
        return self.__home_address
    @property
    def phone_number_home(self) -> int:
        return self.__phone_number_home
    @property
    def phone_number_mobile(self) -> int:
        return self.__phone_number_mobile
    @property
    def email_address(self) -> str:
        return self.__email_address
    @property
    def emergency_contact_primary(self) -> Optional[tuple[str, str, int]]:
        return self.__emergency_contact_primary
    @property
    def emergency_contact_secondary(self) -> Optional[tuple[str, str, int]]:
        return self.__emergency_contact_secondary
    
    def set_emergency_contact(self, name: str, relationship: str, phone_number: str, level: EmergencyContactLevel) -> None:
        if level == EmergencyContactLevel.PRIMARY:
            self.__emergency_contact_primary = (name, relationship, self.phoneNumberFormatter(phone_number))
        elif level == EmergencyContactLevel.SECONDARY:
            self.__emergency_contact_secondary = (name, relationship, self.phoneNumberFormatter(phone_number))
        else:
            raise ValueError("Invalid emergency contact level.")
    
    @full_name.setter
    def full_name(self, name: str) -> None:
        self.__full_name = name
    @date_of_birth.setter
    def date_of_birth(self, dob: str) -> None:
        try:
            self.__date_of_birth = self.dateFormatter(dob)
        except ValueError as e:
            raise ValueError(f"Error parsing 'date_of_birth' date: {e}")  
    @sex.setter
    def sex(self, sex: str) -> None:
        self.__sex = sex
    @home_address.setter 
    def home_address(self, address: str) -> None:
        self.__home_address = address
    @phone_number_home.setter
    def phone_number_home(self, number: str) -> None:
        try:
            self.__phone_number_home = self.phoneNumberFormatter(number)
        except ValueError as e:
            raise ValueError(f"Error parsing 'phone_number_home': {e}")
    @phone_number_mobile.setter
    def phone_number_mobile(self, number: str) -> None:
        try:
            self.__phone_number_mobile = self.phoneNumberFormatter(number)
        except ValueError as e:
            raise ValueError(f"Error parsing 'phone_number_mobile': {e}")
    @email_address.setter
    def email_address(self, email: str) -> None:
        try:
            self.__email_address = self.emailFormatChecker(email)
        except ValueError as e:
            raise ValueError(f"Error parsing 'email_address': {e}")


class Language:
    def __init__(self, language: str, read_ability: str, write_ability: str, speak_ability: str) -> None:
        self.__language = language
        self.__read_ability = read_ability
        self.__write_ability = write_ability
        self.__speak_ability = speak_ability

    @property
    def language(self) -> str:
        return self.__language
    @property
    def read_ability(self) -> str:
        return self.__read_ability
    @property
    def write_ability(self) -> str:
        return self.__write_ability
    @property
    def speak_ability(self) -> str:
        return self.__speak_ability
    
    @language.setter
    def language(self, lang: str) -> None:
        self.__language = lang
    @read_ability.setter
    def read_ability(self, read: str) -> None:
        self.__read_ability = read
    @write_ability.setter
    def write_ability(self, write: str) -> None:
        self.__write_ability = write
    @speak_ability.setter
    def speak_ability(self, speak: str) -> None:
        self.__speak_ability = speak


class Education(InputFormatter):
    def __init__(self, level: EducationLevel, university_name: str, university_location: str, university_country: str, attended_from: str, attended_to: str, certificates: str, main_field_of_study: str) -> None:
        self.__education_level = level
        self.__university_name = university_name
        self.__university_location = university_location
        self.__university_country = university_country
        self.__attended_from = self.dateFormatter(attended_from)
        self.__attended_to = self.dateFormatter(attended_to)
        self.__certificates = certificates.split(',')
        self.__main_field_of_study = main_field_of_study

    @property
    def education_level(self) -> EducationLevel:
        return self.__education_level
    @property
    def university_name(self) -> str:
        return self.__university_name
    @property
    def university_location(self) -> str:
        return self.__university_location
    @property
    def university_country(self) -> str:
        return self.__university_country
    @property
    def attended_from(self) -> datetime.date:
        return self.__attended_from
    @property
    def attended_to(self) -> datetime.date:
        return self.__attended_to
    @property
    def certificates(self) -> list[str]:
        return self.__certificates
    @property
    def main_field_of_study(self) -> str:
        return self.__main_field_of_study
    
    @education_level.setter
    def education_level(self, level: EducationLevel) -> None:
        self.__education_level = level
    @university_name.setter
    def university_name(self, name: str) -> None:
        self.__university_name = name
    @university_location.setter
    def university_location(self, loc: str) -> None:
        self.__university_location = loc
    @university_country.setter
    def university_country(self, country: str) -> None:
        self.__university_country = country
    @attended_from.setter
    def attended_from(self, date: str) -> None:
        try:
            self.__attended_from = self.dateFormatter(date)
        except ValueError as e:
            raise ValueError(f"Error parsing 'attended_from' date: {e}")
    @attended_to.setter
    def attended_to(self, date: str) -> None:
        try:
            self.__attended_to = self.dateFormatter(date)
        except ValueError as e:
            raise ValueError(f"Error parsing 'attended_to' date: {e}")
    @certificates.setter
    def certificates(self, certs: str) -> None:
        new_certificates = certs.split(',')
        if new_certificates != self.__certificates:
            self.__certificates = new_certificates
    @main_field_of_study.setter
    def main_field_of_study(self, main: str) -> None:
        self.__main_field_of_study = main


class WorkExperience(InputFormatter):
    def __init__(self, company: str, location: str, emp_from: str, emp_to: str, position: str, reason: str) -> None:
        self.__company_name = company
        self.__location = location
        self.__emp_from = self.dateFormatter(emp_from)
        self.__emp_to = self.dateFormatter(emp_to)
        self.__position = position
        self.__reason_for_leaving = reason

    @property
    def company_name(self) -> str:
        return self.__company_name
    @property
    def location(self) -> str:
        return self.__location
    @property
    def emp_from(self) -> datetime.date:
        return self.__emp_from
    @property
    def emp_to(self) -> datetime.date:
        return self.__emp_to
    @property
    def position(self) -> str:
        return self.__position
    @property
    def reason_for_leaving(self) -> str:
        return self.__reason_for_leaving
    
    @company_name.setter
    def company_name(self, name: str) -> None:
        self.__company_name = name
    @location.setter
    def location(self, loc: str) -> None:
        self.__location = loc
    @emp_from.setter
    def emp_from(self, emp_from: str) -> None:
        try:
            self.__emp_from = self.dateFormatter(emp_from)
        except ValueError as e:
            raise ValueError(f"Error parsing 'emp_from' date: {e}")
    @emp_to.setter
    def emp_to(self, emp_to: str) -> None:
        try:
            self.__emp_from = self.dateFormatter(emp_to)
        except ValueError as e:
            raise ValueError(f"Error parsing 'emp_to' date: {e}")
    @position.setter
    def position(self, pos: str) -> None:
        self.__position = pos
    @reason_for_leaving.setter
    def reason_for_leaving(self, reason: str) -> None:
        self.__reason_for_leaving = reason


class Applicant(ApplicationBase):
    def __init__(self):
        self.__personal_info: PersonalInfo
        self.__languages: list[Language] = []
        self.__educational_background: list[Education] = []
        self.__work_experience: list[WorkExperience] = []
        self.__major_skills: str

    @property
    def personal_info(self) -> PersonalInfo:
        return self.__personal_info
    @property
    def languages(self) -> list[Language]:
        return self.__languages
    @property
    def educational_background(self) -> list[Education]:
        return self.__educational_background
    @property
    def work_experience(self) -> list[WorkExperience]:
        return self.__work_experience
    @property
    def major_skills(self) -> str:
        return self.__major_skills
    
    @major_skills.setter
    def major_skills(self, skills: str) -> None:
        self.__major_skills = skills

    def add_personal_info(self, full_name: str, date_of_birth: str, sex: str, home_address: str, phone_number_home: str, phone_number_mobile: str, email_address: str) -> None:
        self.__personal_info = PersonalInfo(full_name, date_of_birth, sex, home_address, phone_number_home, phone_number_mobile, email_address)

    def add_language(self, lang: str, read_ability: str, write_ability: str, speak_ability: str) -> None:
        self.__languages.append(Language(lang, read_ability, write_ability, speak_ability))

    def add_education(self, level: EducationLevel,  university_name: str, university_location: str, university_country: str, attended_from: str, attended_to: str, certificates: str, main_field_of_study: str) -> None:
        self.__educational_background.append(Education(level, university_name, university_location, university_country, attended_from, attended_to, certificates, main_field_of_study))

    def add_work_experience(self, company: str, location: str, emp_from: str, emp_to: str, position: str, reason: str) -> None:
        if len(self.__work_experience) < 3:
            self.__work_experience.append(WorkExperience(company, location, emp_from, emp_to, position, reason))

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Applicant):
            return self.personal_info.full_name == __value.personal_info.full_name and self.personal_info.phone_number_mobile == __value.personal_info.phone_number_mobile
        return False
    
    def __hash__(self) -> int:
        return hash((self.personal_info.full_name, self.personal_info.phone_number_mobile))


class Application:
    def __init__(self) -> None:
        self.__applicants: list[Applicant] = []

    @property
    def applicants(self) -> list[Applicant]:
        return self.__applicants

    def __iter__(self):
        self.index = -1
        return self
    
    def __next__(self):
        self.index += 1
        if self.index >= len(self.__applicants):
            raise StopIteration
        return self.__applicants[self.index]

    def add_applicant(self, applicant: Applicant) -> None:
        if applicant not in self.__applicants:
            self.__applicants.append(applicant)
            print("*****######******######*******######")
            print("Application added successfully!")
            print("*****######******######*******######")
        else: 
            print("*****######******######*******######")
            print("You have already applied for this job!")
            print("*****######******######*******######")

    def search_application(self, full_name: str) -> list[Applicant]:
        found_applicants: list[Applicant] = []
        for applicant in self.__applicants:
            if applicant.personal_info.full_name.lower() == full_name.lower():
                found_applicants.append(applicant)
        return found_applicants

    def update_application(self, full_name: str, new_applicant: Applicant) -> None:
        for i in range(len(self.__applicants)):
            if self.__applicants[i].personal_info.full_name.lower() == full_name.lower():
                self.__applicants[i] = new_applicant
                print("*****######******######*******######")
                print("Application updated successfully!")
                print("*****######******######*******######")
            else:
                print("*****######******######*******######")
                print(f"Applicant with name '{full_name}' doesn't exist!")
                print("*****######******######*******######")

    def delete_application(self, full_name: str) -> None:
        for applicant in self.__applicants:
            if applicant.personal_info.full_name.lower() == full_name.lower():
                self.__applicants.remove(applicant)
                print("*****######******######*******######")
                print("Application deleted successfully!")
                print("*****######******######*******######")
            else: 
                print("*****######******######*******######")
                print(f"Applicant with name '{full_name}' doesn't exist!")
                print("*****######******######*******######")
                
    def display_applications(self, applicants: list[Applicant]):
        output = ""
        if len(applicants) != 0:
            i = 1  
            for applicant in applicants:
                output = "\n*****######******######*******######"
                output += f"\n\n*****  Application {i}  *****\n\n"
                output += "*****######******######*******######\n\n"
                output += f"Full Name: {applicant.personal_info.full_name}\n"
                output += f"Date of Birth: {applicant.personal_info.date_of_birth}\n"
                output += f"Sex: {applicant.personal_info.sex}\n"
                output += f"Home Address: {applicant.personal_info.home_address}\n"
                output += f"Phone number (home): {applicant.personal_info.phone_number_home}\n"
                output += f"Phone number (mobile): {applicant.personal_info.phone_number_mobile}\n"
                output += f"Email Address: {applicant.personal_info.email_address}\n\n"
                output += "-----  Languages:  -----\n\n"
                for lang in applicant.languages:
                    output += f"Language: {lang.language}\n"
                    output += f"Read Ability: {lang.read_ability}\n"
                    output += f"Write Ability: {lang.write_ability}\n"
                    output += f"Speak Ability: {lang.speak_ability}\n\n"
                output += "-----  Educational Background:  -----\n\n"
                for edu in applicant.educational_background:
                    output += f"University Name: {edu.university_name}\n"
                    output += f"University Location: {edu.university_location}\n"
                    output += f"University Country: {edu.university_country}\n"
                    output += f"Attended from: {edu.attended_from}\n"
                    output += f"Attended till: {edu.attended_to}\n"
                    output += f"Certificates list: {', '.join(edu.certificates)}\n"
                    output += f"Main field of study: {edu.main_field_of_study}\n\n"
                output += "\n-----  Work Experience:  -----\n\n"
                for experience in applicant.work_experience:
                    output += f"Company: {experience.company_name}\n"
                    output += f"Location: {experience.location}\n"
                    output += f"Employed from: {experience.emp_from}\n"
                    output += f"Employed till: {experience.emp_to}\n"
                    output += f"Position: {experience.position}\n"
                    output += f"Reason for leaving: {experience.reason_for_leaving}\n\n"
                output += f"Major Skills: {applicant.major_skills}\n"
                print(output)
                i += 1
        if not output:
            print("*****######******######*******######")
            print("No applications found!")
            print("*****######******######*******######")


def main():

    application = Application()
    error_counter = 0

    def select_education_level() -> EducationLevel:
        # Create a dictionary to map indices to EducationLevel enum values
        index_to_level: dict[int, EducationLevel] = {i + 1: level for i, level in enumerate(EducationLevel)}
        
        print("Select your education level:")
        for i, level in index_to_level.items():
            print(f"{i}. {level.value}")
        
        while True:
            choice = input("Enter the number corresponding to your choice: ")
            try:
                choice_index = int(choice)
                if choice_index in index_to_level:
                    return index_to_level[choice_index]
                else:
                    print(f"Invalid choice. Please enter a number between 1 and {len(index_to_level)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def createApplicant() -> Applicant:
        applicant = Applicant()
        try:
            applicant.add_personal_info(
                input("Full Name: "),
                input("Date of Birth (YYYY-MM-DD): "),
                input("Sex (Male/Female): "),
                input("Home Address: "),
                input("Phone number (home): "),
                input("Phone number (mobile): "),
                input("Email Address: ")
            )
        except ValueError:
            raise ValueError
        try:
            print("Enter primary emergency contact: ")
            for _ in range(2):
                if _ == 0:
                    contactLevel = EmergencyContactLevel.PRIMARY
                    msg = "Enter secondary emergency contact: "
                else:
                    contactLevel = EmergencyContactLevel.SECONDARY
                    msg = None
                applicant.personal_info.set_emergency_contact(
                    input("Emergency Contact Full Name: "),
                    input("Relationship with Contact: "),
                    input("Phone number of Emergency Contact: "),
                    contactLevel 
                )
                if msg:
                    print(msg)
        except ValueError:
            raise ValueError
        while True:
            applicant.add_language(
                input("Language: "),
                input("Ability to Read (excellent/good/bad): "),
                input("Ability to Write (excellent/good/bad): "),
                input("Ability to Speak (excellent/good/bad): ")
            )
            if input("Do you want to add language (y/n)? ").lower() == "n":
                break
        try:
            while True:
                applicant.add_education(
                    select_education_level(),
                    input("School name: "),
                    input("School location: "),
                    input("School country: "),
                    input("Attended from (YYYY-MM-DD): "),
                    input("Attended till (YYYY-MM-DD): "),
                    input("Certificates list (comma-separated): "),
                    input("Main field of study: ")
                )
                if input("Do you want to add education (y/n)? ").lower() == "n":
                    break
        except ValueError:
            raise ValueError
        try:
            for _ in range(3):    
                if input("Do you want to add work experience (y/n)? ").lower() == "n":
                    break
                applicant.add_work_experience(
                    input("Company Name: "),
                    input("Location: "),
                    input("Employed from (YYYY-MM-DD): "),
                    input("Employed till (YYYY-MM-DD): "),
                    input("Position: "),
                    input("Reason for leaving: ")
                )
        except ValueError:
            raise ValueError
        applicant.major_skills = input("Major skills (comma-separated):")
        return applicant

    while True:
        print("\n*****######*****######*****######*****######*****######******######*******######")
        print("\tWelcome to the Career Training Institution Application Manager")
        print("*****######*****######*****######*****######*****######******######*******######")
        print("\t\t1. Add Application")
        print("\t\t2. Search Application")
        print("\t\t3. Update Application")
        print("\t\t4. Delete Application")
        print("\t\t5. Display All Applications")
        print("\t\t6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                application.add_applicant(createApplicant())
            except ValueError as e:
                error_counter += 1
                print(e)
            except Exception as e:
                error_counter += 1
                print(f"{type(e).__class__}: {e}")
            if error_counter < 3:
                continue
            else:
                print("\n*****######******######*******######")
                print("Too many bad attempts. Please try again later!")
                print("\n*****######******######*******######")
                break

        elif choice == "2":
            full_name = input("Enter Full Name to search: ")
            search_result = application.search_application(full_name)
            if search_result:
                print("\n*****######******######*******######")
                print("Search Results:")
                application.display_applications(search_result)
            else: 
                print("*****######******######*******######")
                print(f"Applicant with name '{full_name}' doesn't exist!")
                print("*****######******######*******######")

        elif choice == "3":
            full_name = input("Enter Full Name to update: ")
            search_result = application.search_application(full_name)
            if not search_result:
                print("*****######******######*******######")
                print(f"Application with name '{full_name}' doesn't exist!")
                print("*****######******######*******######")
            else:
                application.update_application(full_name, createApplicant())
                
        elif choice == "4":
            full_name = input("Enter Full Name to delete: ")
            application.delete_application(full_name)

        elif choice == "5":
            application.display_applications(application.applicants)

        elif choice == "6":
            print("Bye!")
            break


if __name__ == "__main__":
    main()
