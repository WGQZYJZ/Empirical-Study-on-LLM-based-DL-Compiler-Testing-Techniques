
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(torch.randn(3))
        self.dropout  = torch.nn.Dropout()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) * self.scale 
        v2  = torch.softmax(v1, dim=-1) 
        v3  = self.dropout(v2)
        v4  = v3 @ value  
        return v4


# Initializing the model
m  = Model()

 # Inputs to the model
x0_1  = torch.randn(56, 728).to('cuda')
x0_2  = torch.randn(56, 728).to('cuda')
x0_3  = torch.randn(496, 56).to('cuda')

 # Initial values for the parameters of the model
x1  = {
    'scale': torch.tensor([[-0.1087], [-0.4257], [ -0.346]], device='cuda', requires_grad=True), 
    'dropout': torch.nn.Dropout(inplace=False, p=0.9).eval()
}

 # Running the model with input tensors and initial values as inputs to the model
with torch.no_grad():
    __output__  = m(x0_1, x0_2, x0_3)
