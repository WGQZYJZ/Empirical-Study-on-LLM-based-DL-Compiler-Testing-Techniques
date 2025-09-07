
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1, x2):
        q1  = self.linear1(x1)
        k1  = self.linear1(x2)
        v1  = self.linear1(torch.zeros_like(k1))
        q2  = torch.nn.functional.dropout(q1, p=self.p)
        k2  = torch.nn.functional.dropout(k1, p=self.p)
        scaled_qk  = q2 * k2
        softmax_qk  = scaled_qk.softmax(-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self.p)
        output  = dropout_qk.matmul(v1)
        return self.linear2(output)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
