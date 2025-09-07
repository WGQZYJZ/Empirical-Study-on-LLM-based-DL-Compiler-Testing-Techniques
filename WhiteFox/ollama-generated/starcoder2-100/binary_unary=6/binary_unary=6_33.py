
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64, bias=False)
 
    def forward(self, x1):
        v0  = x1[:, :, 1] + 0.5 # add 0.5 to the first channel of each input sample. Note that it's different from "other" in the previous scenario because the value is added to all samples at once and the result is broadcasted over channels as a whole, whereas "other" is only added per sample individually
        v1 = self.linear(x0) # Applying a linear transformation with 32 input features and 64 output features
        v2 = v1 - other
        v3 = torch.nn.functional.relu(v2) # Applying the ReLU function to the result
        return v3


# Initializing model
m  = Model()

# Inputs to model
x0 = torch.randn(8, 32, 16)
