In this pattern, the output of a layer is usually added to another tensor (like in the residual connections). In this case, the keyword argument "other" is an input tensor, and not a model's parameter.

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(320, 512)
        self.linear2 = torch.nn.Linear(512, 320)
 
    def forward(self, x):
        return x + self.linear2(self.linear1(x))


# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where two tensors are multiplied, and then the output of the linear transformation is multiplied by that of another tensor. In this case, the keyword argument "other" is an input tensor, and not a model's parameter.

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(320, 512)
        self.linear2 = torch.nn.Linear(512, 320)
 
    def forward(self, x1, x2=None):
        if x2 is not None:
            v1 = x1 * x2  # Multiply the input tensors 1 with their respective inputs of 2
        else:
            v1 = x1 * self.linear1.weight
        v2 = v1 * self.linear1.bias
        return v2


# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where a linear transformation is applied to an input tensor, and then another tensor (specified by the keyword argument "other") is added to the output of the linear transformation. In this case, the keyword argument "other" is an input tensor, not a model's parameter.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(320, 512)
        self.linear2 = torch.nn.Linear(512, 320)
 
    def forward(self, x):
        return (x + 2 * self.linear2(self.linear1(x))) / 3


# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where two tensors are multiplied, and then the output of the linear transformation is multiplied by that of another tensor. In this case, the keyword argument "other" is an input tensor, not a model's parameter.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(320, 512)
        self.linear2 = torch.nn.Linear(512, 320)
 
    def forward(self, x1, x2=None):
        if x2 is not None:
            v1 = x1 * (x2 + 1)  # Multiply the input tensors 1 with their respective inputs of 2
        else:
            v1 = (x1 + 1) * self.linear1.weight
        v2 = v1 * self.linear1.bias
        return v2


# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where two tensors are added together. In this case, the keyword argument "other" is an input tensor, not a model's parameter.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(320, 512)
        self.linear2 = torch.nn.Linear(512, 320)
 
    def forward(self, x):
        v1 = x * (x + 1)  # Multiply the input tensor with its respective inputs of 2 and add another input tensor
        v2 = v   ... . .
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--------------------------------------------------------------
