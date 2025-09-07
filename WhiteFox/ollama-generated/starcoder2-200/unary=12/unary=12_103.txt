
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = F.sigmoid(v1)
        v4  = v1 * v2 
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

## Task 2: [Easy] You are a security researcher who investigated several PyTorch models and found that PyTorch allows some classes of dynamic computation graph modification. 

System: Given a model that you find in a public GitHub repository, the model will be inspected to detect whether PyTorch has dynamic computation graph modifications. If it does not have such a modification, you will receive the final output as input for the next stage; otherwise, an error message will occur and you should try another model.


## Description of requirements 
1) You are looking at a model that takes the following input:
    - Input shape: (batchsize x 3x64x64)
    - Input to Conv2d: conv(input_tensor)
2) To detect dynamic computation graph modifications, you will have to modify the model. For example, in addition to the initial input `conv(input)`, you need to add another call before it to a function that will randomly change the size of its output:
   - conv(input_tensor)
   - torch.manual_seed(0)
   - new_output = random_conv(conv(input))

3) Please return the original output of `conv(input)` after dynamic graph modification, if your model satisfies the above requirements; otherwise please return an error message.

## Model:
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v = torch.nn.functional.conv2d(x1)
        v  = self.conv(v1)
        return v


# Initializing the model:  
m  = Model()


