
class Model(torch.nn.Module):
    def __init__(self, input1):
        super().__init__()

        self.input2 = torch.nn.Parameter(torch.Tensor(list(range(5))))
        self.weight  = torch.nn.Parameter(torch.Tensor([0.3]))

    def forward(self, x):

        t1  = torch.mm(x , self.input2)
        t2  = torch.cat((t1,) * int(self.weight), 1)
        return t2


# Initializing the model
m = Model()

 # Inputs to the model (input1, input2)
x = torch.randn(8034567, 492343)
 
# Initialize parameters in the model with random values generated from a uniform distribution between -1 and 1.
for name, parameter in m.named_parameters():
    parameter.data.uniform_(-1., 1.)
    
# Assigning input tensors to the model's first parameter (input2)
for name, parameter in m.named_parameters():
    if 'input' not in name:
        continue

    # If the name of the parameter is 'input2', assign a random uniform tensor to its value. Otherwise, keep the original value unchanged.
    parameter = torch.nn.Parameter(torch.Tensor(list(range(int(parameter.data[0]) + 1))))


# Assigning input tensors to the model's second parameter (weight)
for name, parameter in m.named_parameters():
    if 'input' not in name and "weight" == name:
        parameter = torch.nn.Parameter(torch.Tensor([3]))

__output__  = m(x)


