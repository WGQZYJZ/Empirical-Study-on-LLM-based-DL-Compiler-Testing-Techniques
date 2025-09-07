
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.linear1(x1)  # [batch_size, seq_len, d_model]
        v2 = self.linear2(v1).contiguous()  # [batch_size, seq_len, d_head]
        return torch.softmax(v2, dim=-1)


# Initializing the model
m = Model()

