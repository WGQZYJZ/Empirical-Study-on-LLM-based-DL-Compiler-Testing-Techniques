
class Model2(torch.nn.Module):
    def __init__(self, input_size=3, hidden1_size=8, hidden2_size=64, output_size=10):
        super().__init__()

        self.linear = torch.nn.Linear(input_size, hidden1_size)
        self.linear2  = torch.nn.Linear(hidden1_size, hidden2_size) # This model is different from the previous one by using a linear transformation of size (8,64)
        self.output  = torch.nn.Linear(hidden2_size, output_size)

    def forward(self, x):
        
        v1 = self.linear(x)
        v2 = v1 + other # Add another tensor to the output of the linear transformation
        
        return v2


# Initializing the model
m  = Model2()


# Inputs to the model
x1 = torch.randn(1, 3)
__output__  = m(x1)

