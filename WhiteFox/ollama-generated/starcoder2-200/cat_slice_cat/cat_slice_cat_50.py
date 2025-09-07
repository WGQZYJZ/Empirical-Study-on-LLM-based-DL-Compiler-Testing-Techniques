
class Model(torch.nn.Module):
    def __init__(self, size=9223372036854775807):
        super().__init__()
        
    def forward(self, x1s):
        v = []  # Define the list of tensors as an array of dimension one with name v
        for x in x1s:
            v.append(x)  # Append each input tensor to the list of tensors
        v2 = torch.cat(v, dim=0) 
        v3 = v2[:, :9223372036854775807]  
        v4 = v3[:,:size]
        v5  = torch.cat([v2, v4], dim=1)
        return v5


# Initializing the model