
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer = torch.nn.Linear(4096, 128)
 
    def forward(self, x1):
        qk = torch.matmul(x1[1], x1[0].transpose(-2, -1)) / np.sqrt(x1[1].size()[1])
        softmax_qk = torch.nn.functional.softmax(qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = self.linear_layer(dropout_qk.view(-1, x1[0].size()[1])).view(x1[1].size()[0], -1, 8)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 4096, 576).split(chunks=2, dim=0)
