
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1, 2)
 
    def forward(self, qk):
        v1 = self.query(qk[0]) + self.query(qk[1])
        softmax_v1 = F.softmax(v1)
        dropout_v1 = torch.nn.functional.dropout(softmax_v1, p=dropout_p)
        output  = dropout_v1 * qk[2]
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk = [torch.randn(32), torch.randn(64), torch.randn(32)]
