

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale_factor=None, dropout_p=None):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v3 = torch.nn.functional.normalize(v1)
        return v2

# Initializing the model
m = Model()
 
# Input tensors to the model
q_tensor = torch.randn(100, 64, 512).cuda().requires_grad_()
k_tensor = torch.randn(100, 512, 64).cuda().requires_grad_()
v_tensor = torch.randn(100, 512, 768)
 
# Running the model
with torch.no_grad():
    q = m(q_tensor, k_tensor, v_tensor)
