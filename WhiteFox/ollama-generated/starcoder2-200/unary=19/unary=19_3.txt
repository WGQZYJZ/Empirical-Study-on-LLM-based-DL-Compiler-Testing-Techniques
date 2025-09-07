
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(4096, 32) # 4096 is the batch size; you can change it based on your needs or the scenario


# Outputs from the model
__output__  = m(x1).data # .data is to avoid unnecessary tensors being added and saturated. The output is a 5 dimensional vector that contains probability values between 0 and 1.

