
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48*64**2+1050, 37)

    def forward(self, x):
        v1 = torch.reshape(x[:, :48], [v1.shape[0], -1]) 
        v2 = torch.cat([v1, x[:,-1]], axis=1).type(torch.FloatTensor)
        v3 = self.linear(v2)
        return  F.sigmoid(v3)


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn([5, 48*64**2+1050]) # A batch of inputs where each row is an example with 1050 features and a label at index -1; note that this input is different from previous one.
__output__  = m(x)

