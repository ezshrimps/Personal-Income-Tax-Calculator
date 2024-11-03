class Employee:
    def __init__(self, monthly_income, social_security, housing_fund, num_children=0, education_deduction=0, medical_expenses=0, mortgage_interest=0, rent=0, elderly_support=0, is_only_child=False):
        self.monthly_income = monthly_income
        self.social_security = social_security
        self.housing_fund = housing_fund
        self.num_children = num_children
        self.education_deduction = education_deduction
        self.medical_expenses = medical_expenses
        self.mortgage_interest = mortgage_interest
        self.rent = rent
        self.elderly_support = elderly_support
        self.is_only_child = is_only_child

    def calculate_tax(self):
        # 起征点
        threshold = 5000

        # 子女教育专项附加扣除
        children_deduction = 1000 * self.num_children

        # 继续教育专项附加扣除
        education_deduction = self.education_deduction

        # 大病医疗专项附加扣除
        if self.medical_expenses > 15000:
            medical_deduction = min(self.medical_expenses - 15000, 80000)
        else:
            medical_deduction = 0

        # 住房贷款利息专项附加扣除
        mortgage_deduction = self.mortgage_interest

        # 住房租金专项附加扣除
        rent_deduction = self.rent

        # 赡养老人专项附加扣除
        if self.is_only_child:
            elderly_deduction = 2000
        else:
            elderly_deduction = min(self.elderly_support, 1000)

        # 应纳税所得额计算
        taxable_income = (self.monthly_income - threshold - self.social_security - self.housing_fund - children_deduction - education_deduction - medical_deduction - mortgage_deduction - rent_deduction - elderly_deduction)

        if taxable_income <= 0:
            return 0

        # 税率表
        tax_brackets = [
            (36000, 0.03, 0),
            (144000, 0.10, 2520),
            (300000, 0.20, 16920),
            (420000, 0.25, 31920),
            (660000, 0.30, 52920),
            (960000, 0.35, 85920),
            (float('inf'), 0.45, 181920)
        ]

        # 查找适用税率和速算扣除数
        annual_taxable_income = taxable_income * 12
        for limit, rate, quick_deduction in tax_brackets:
            if annual_taxable_income <= limit:
                tax_rate = rate
                deduction = quick_deduction
                break

        # 个税计算公式
        annual_tax = annual_taxable_income * tax_rate - deduction
        monthly_tax = annual_tax / 12

        return monthly_tax

# 示例使用
if __name__ == "__main__":
    # 创建员工实例
    employee1 = Employee(
        monthly_income=10000,  # 月收入
        social_security=500,   # 社保缴纳
        housing_fund=500,      # 公积金缴纳
        num_children=1,        # 子女数量
        education_deduction=0,  # 继续教育扣除
        medical_expenses=0,     # 大病医疗支出
        mortgage_interest=0,    # 住房贷款利息
        rent=0,                 # 住房租金
        elderly_support=0,      # 赡养老人支出
        is_only_child=True      # 是否独生子女
    )

    # 调用计算个税的方法
    monthly_tax = employee1.calculate_tax()
    print(f"每月应缴个税：{monthly_tax:.2f} 元")
