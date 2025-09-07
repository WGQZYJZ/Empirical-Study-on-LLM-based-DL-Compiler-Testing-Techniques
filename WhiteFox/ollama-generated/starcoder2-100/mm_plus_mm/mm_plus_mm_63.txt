
class Model(torch.nn.Module):
    def __init__(self, input1, input2, input3, input4):
        super().__init__()
 
    def forward(self, v1):
        v2  = torch.mm(v1, self.input1) +  # Matrix multiplication between the output of the previous layer and input1
                torch.mm(v1, self.input2)  # Addition of the results from two matrix multiplications between the output of the previous layer and inputs3
        return v2

# Initializing model with different inputs to the modules
m = Model(input1=input_tensor, input2=input_tensor2, 
            input3=input_tensor3, input4=input_tensor4)  # The first argument will be used as the input for the layer conv

