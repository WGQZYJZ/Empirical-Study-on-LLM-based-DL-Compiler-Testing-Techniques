
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(20, 5)
        self.linear2 = torch.nn.Linear(483, 79)

    def forward(self, x1):

        v1 = torch.nn.functional.linear(x1,  self.linear1.weight,  None).permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1 ,  self.linear2 . weight,  None).permute(0, 3, 1, 2)
        return v2


# Initializing the model
m  = Model()



# Inputs to the model
x1 = torch.randn(579, 20)


# Input tensors for the 3 models
## [input_tensor_1, output tensor of the model] ##
## [input_tensor_2, output tensor of the model] ##
## [input_tensor_3, output tensor of the model] ##
t1 = torch.randn(579, 8)

t4  = x1
t3 = t4  . permute (0 , 1 )
## [model, input to the model, expected output from the model for the input, permuted input tensor of the model] ##

