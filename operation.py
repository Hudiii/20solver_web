import itertools

# pembuatan class untuk kombinasi pertama dari 2 operand
class combination_1():
    def __init__(self, operand_1, operand_2):

        self._operand_1_ = operand_1
        self._operand_2_ = operand_2

        if (isinstance(operand_1, combination_1)):
            self.operand_1 = operand_1.dat
        else:
            self.operand_1 = operand_1
        if (isinstance(operand_2, combination_1)):
            self.operand_2 = operand_2.dat
        else:
            self.operand_2 = operand_2

    def __str__(self):
        return self.fmt.format(self._operand_1_, self._operand_2_)

    def __eq__(self, other):
        return not self.dat < other and not other < self.dat

# pengecekan kemungkinan kombinasi pertama dengan penjumlahan (2 operand)
class combination_1_add(combination_1):
    def __init__(self, operand_1, operand_2):
        super().__init__(operand_1, operand_2)
        self.dat = self.operand_1 + self.operand_2
        self.fmt = '( {0} + {1} )'

# pengecekan kemungkinan kombinasi pertama dengan penjumlahan (2 operand)
class combination_1_sub(combination_1):
    def __init__(self, operand_1, operand_2):
        super().__init__(operand_1, operand_2)
        self.dat = self.operand_1 - self.operand_2
        self.fmt = '( {0} - {1} )'

# pengecekan kemungkinan kombinasi pertama dengan penjumlahan (2 operand)
class combination_1_mul(combination_1):
    def __init__(self, operand_1, operand_2):
        super().__init__(operand_1, operand_2)
        self.dat = self.operand_1 * self.operand_2
        self.fmt = '( {0} * {1} )'

# pengecekan kemungkinan kombinasi pertama dengan penjumlahan (2 operand)
class combination_1_div(combination_1):
    def __init__(self, operand_1, operand_2):

        super().__init__(operand_1, operand_2)
        if self.operand_2 == 0:
            self.dat = 1000
        else:
            self.dat = self.operand_1 / self.operand_2
        self.fmt = '( {0} / {1} )'

# pengecekan kemungkinan kombinasi kedua dengan 3 operand (penggunaan tanda kurung)
def combination_2a(operand_1, operand_2, operand_3,
               oper_1, oper_2):
    return oper_1(operand_1, oper_2(operand_2, operand_3))

# pengecekan kemungkinan kombinasi kedua dengan 3 operand (penggunaan tanda kurung)
def combination_2b(operand_1, operand_2, operand_3,
               oper_1, oper_2):
    return oper_1(oper_2(operand_1, operand_2), operand_3)

# pengecekan kemungkinan kombinasi dengan semua operand dan 3 jenis operasi dengan tanda kurung
def combination_3a(operand_1, operand_2, operand_3, operand_4,
               oper_1, oper_2, oper_3):
    return oper_1(
        combination_2a(operand_1, operand_2, operand_3, oper_2, oper_3), operand_4)

# pengecekan kemungkinan kombinasi lain dengan semua operand 
def combination_3b(operand_1, operand_2, operand_3, operand_4,
               oper_1, oper_2, oper_3):
    return oper_1(
        combination_2b(operand_1, operand_2, operand_3, oper_2, oper_3), operand_4)

# pengecekan kemungkinan kombinasi lain dengan semua operand 
def combination_3c(operand_1, operand_2, operand_3, operand_4,
               oper_1, oper_2, oper_3):
    return oper_1(
        operand_1, combination_2a(operand_2, operand_3, operand_4, oper_2, oper_3))

# pengecekan kemungkinan kombinasi lain dengan semua operand 
def combination_3d(operand_1, operand_2, operand_3, operand_4,
               oper_1, oper_2, oper_3):
    return oper_1(
        operand_1, combination_2b(operand_2, operand_3, operand_4, oper_2, oper_3))

# pengecekan kemungkinan kombinasi lain dengan semua operand 
def combination_3e(operand_1, operand_2, operand_3, operand_4,
               oper_1, oper_2, oper_3):
    return oper_1(
        oper_2(operand_1, operand_2), oper_3(operand_3, operand_4))

#
combination_1_classes = [combination_1_add, combination_1_sub, combination_1_mul, combination_1_div]

combination_3_operations = [combination_3a, combination_3b, combination_3c, combination_3d, combination_3e]

def calc(input):
    operation_result = []
    operands_all = set(itertools.permutations(input))
    operands_combination_1_iter = list(itertools.product(combination_1_classes, repeat=3))
    for operands in operands_all:
        for combination in operands_combination_1_iter:
            for combination_final in combination_3_operations:
                result = combination_final(*(operands + combination))
                if result == 20:
                    operation_result.append(str(result))
    return operation_result