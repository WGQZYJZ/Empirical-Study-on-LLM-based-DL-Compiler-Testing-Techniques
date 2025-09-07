
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 4)
 
    def forward(self, x1, y1):
        v1  = self.linear(x1) + y1
        return v1


# Initializing the model
m2  = Model2()

# Inputs to the model
input_tensor1 = torch.randn(10, 8)
__input1__ = input_tensor1
input_tensor2 = torch.zeros(5).float().to('cuda') + y1
y1  = torch.randn(1, 4).float() - m2(x1, y1)

