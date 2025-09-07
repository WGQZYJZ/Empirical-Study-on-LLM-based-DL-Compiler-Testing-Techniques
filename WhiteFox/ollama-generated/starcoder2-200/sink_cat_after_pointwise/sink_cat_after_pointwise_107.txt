
class Model(torch.nn.Module):
    def __init__(self, hidden_size=256):
        super().__init__()

        self.embedding = torch.nn.Embedding(10, 3)
        self.lstm = torch.nn.LSTMCell(input_size=3,
                                      hidden_size=hidden_size)
        self.linear = torch.nn.Linear(in_features=hidden_size + 3, out_features=4)

    def forward(self, x):
        v1 = x.permute((0, 2, 1))
        v2 = v1[:, :, :x.shape[0]].float()

        # t1 = torch.cat([tensor1, tensor2], dim=-3).float()
        # t2 = t1.view(t1.shape[-4] + ...).float()
        v3 = self.embedding(v2)  # apply pointwise unary op.
        return v3


m  = Model()

inputs  = torch.randn([7, 3])
outputs = m(inputs)

