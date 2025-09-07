
class Model(torch.nn.Module):
    def __init__(self, dim_q=512, dim_k=64):
        super().__init__()
        self.linear = torch.nn.Linear(dim_q, dim_k)
 
    def forward(self, q, k, v):
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) * scale_factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        output = dropout_p * softmax_qk.matmul(v)
        return output


# Initializing the model
m = Model()
q = torch.randn(1024, 512, 64, 64)
k = torch.randn(1024, 64, 64, 64)
v = torch.randn(1024, 64, 64, 64)
