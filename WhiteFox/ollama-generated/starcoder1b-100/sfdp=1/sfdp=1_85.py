
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        kq = torch.matmul(x2, x1.transpose(-2, -1)) / math.sqrt(float(torch.tensor(4), device=device))
        sqk = kq.div(math.sqrt(float(torch.tensor(16), device=device)))
        softmax_sqk = sqk.softmax(dim=-1)
        dropout_sqk = torch.nn.functional.dropout(softmax_sqk, p=dropout_p)
        output = dropout_sqk.matmul(x1)
        return output


# Initializing the model
m  = Model()


