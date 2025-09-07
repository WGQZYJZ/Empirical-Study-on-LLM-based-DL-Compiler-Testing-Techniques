
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Split operation in dimension 3 (x1.shape[-1])
        a = torch.split(x1, [256], dim=3)
        b = torch.cat([a[0], x1[:, :, :,:9]],dim=-1)
        
        # Concatenation operation
        return b
 
# Initialize the model 
m = Model()

# Inputs to the model
x1 = torch.zeros(8, 4, 576, 3200).cuda()
__output__  = m(x1)

