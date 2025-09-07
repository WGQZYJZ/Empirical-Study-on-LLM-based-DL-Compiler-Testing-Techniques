
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, torch.zeros_like(v1))  # Select the output of the linear transformation with a threshold value less than or equal to 0
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(4, 4)  # 4 rows and 4 columns of random floats in [-1, 1]
