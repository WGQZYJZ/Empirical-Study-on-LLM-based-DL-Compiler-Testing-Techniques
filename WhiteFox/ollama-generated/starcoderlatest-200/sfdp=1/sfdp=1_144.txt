
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(32 * 64, 32)
        self.linear_k = torch.nn.Linear(32 * 64, 32)
        self.linear_v = torch.nn.Linear(32 * 64, 32)
 
    def forward(self, q1, k1, v1):
        t1 = torch.matmul(q1, k1.transpose(-2, -1))
        t2 = t1 / 0.028571429
        t3 = torch.nn.functional.softmax(t2, dim=-1)
        t4 = torch.nn.functional.dropout(t3, p=dropout_p)
        t5 = torch.matmul(t4, v1)
        return t5
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 32 * 64, 1, 1)
y1 = torch.randn(1, 32 * 64, 1, 1)
z1 = torch.randn(1, 32 * 64, 1, 1)
