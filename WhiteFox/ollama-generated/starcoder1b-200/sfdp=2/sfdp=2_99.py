
class Model(torch.nn.Module):
    def __init__(self, dim=8):
        super().__init__()
        self.query = torch.nn.Linear(dim, 4)
        self.key = torch.nn.Linear(dim, 4)
        self.value = torch.nn.Linear(dim, 4)
        self.scale_factor = torch.nn.Parameter(torch.ones(1))
 
    def forward(self, qk):
        dropout_qk = torch.nn.functional.dropout(qk.matmul(self.scale_factor), p=dropout_p)
        output = dropout_qk.matmul(self.value).matmul(self.key.transpose(-2, -1))
        return output


# Initializing the model
m = Model()
m.scale_factor.data[0] = 3
