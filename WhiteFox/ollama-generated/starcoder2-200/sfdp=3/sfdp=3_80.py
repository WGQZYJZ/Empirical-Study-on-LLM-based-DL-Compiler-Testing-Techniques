
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1  = torch.matmul(input1, input2.transpose(-2, -1)) 
        v2  = v1 * scale_factor  
        v3  = v2.softmax(dim=-1)   
        v4  = torch.nn.functional.dropout(v3, p=0.5) 
        v5  = v4.matmul(input2)
        return v5


# Initializing the model
m = Model()
 
 # Inputs to the model
input1 = torch.randn(8, 128, 16)
input2 = torch.randn(320, 128, 768)
 
