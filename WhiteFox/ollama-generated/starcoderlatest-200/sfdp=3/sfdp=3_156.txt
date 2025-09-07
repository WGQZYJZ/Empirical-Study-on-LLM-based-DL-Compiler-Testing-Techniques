
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(128, 64)
        self.linear_k = torch.nn.Linear(128, 64)
        self.linear_v = torch.nn.Linear(128, 64)
 
    def forward(self, qk):
        v5 = torch.matmul(qk, self.linear_v(query))
        output = torch.matmul(softmax_qk, value) * self.linear_v(query)
        return output


# Initializing the model
m = Model()

