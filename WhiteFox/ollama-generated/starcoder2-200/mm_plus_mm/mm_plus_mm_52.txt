
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1  = torch.mm(x1, x2) 
        v2  = torch.mm(x3, x4) 
        v3  = v1 + v2  
        return v3


# Initializing the model
m  = Model()
input1 = torch.randn([8096])
input2 = torch.randn([1572864], [1200,1024])
 
# Inputs to the model: input3 and input4 must be different than the previous inputs. The model should contain 2 unique input tensors (different from each other).
input3 = torch.randn(1025)
input4 = torch.randn([768, 196], [8096])

 # Initializing the model with 2 unique input tensors and getting the outputs from the model: output of the first model should not be identical to that of the second model
__output_1__ = m(input1, input2, input3, input4)
model_input3 = [input3] + [input4]
 
# Generating a second model with 2 unique input tensors and getting outputs from it. The output should be different than that of the previous model generated. This is a required test for ensuring that there are multiple unique input tensors used by the model. The model should not contain 1 input tensor (the one used in the first model).
model_input3 = [input2] + [input4]
 
# Output from the first model, used to compare with output of second model generated above. The output should be different than that of the first model. This is a required test for ensuring that there are multiple unique input tensors used by the model and that they are being passed to it.
__output_2__ = m(input1, input3, input4)
