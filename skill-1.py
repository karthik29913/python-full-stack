class students:
    def init(self, s_id, s_fname, s_lname, cr, y, gpa, uni, email, mob):
        self.s_id = s_id
        self.s_fname = s_fname
        self.s_lname = s_lname
        self.cr = cr
        self.y = y
        self.gpa = gpa
        self.uni = uni
        self.email = email
        self.mob = mob

    def names(self):
        return self.s_fname, self.s_lname

    def id(self):
        return self.s_id

    def course(self):
        return self.cr

    def year(self):
        return self.y

    def gpa(self):
        return self.gpa

    def university(self):
        return self.uni

    def Email(self):
        choice = int(input("1 for auto generated email 0 for custom email: "))
        if choice == 1:
            return self.s_fname + self.s_lname + "@gmail.com"
        else:
            return self.email

    def mobile(self):
        return self.mob


one = students(1, "bharath", "b", "aids", 2020, 9.2, "klu", "123@gmail.com", 1234567)
two = students(2, "karthikeyan", "n", "aids", 2020, 8.9, "klu", "324@gmail.com", 4566789)
three = students(3, "vijay", "ch", "aids", 2020, 9.0, "klu", "567@gmail.com", 7891234)
print(one.Email())