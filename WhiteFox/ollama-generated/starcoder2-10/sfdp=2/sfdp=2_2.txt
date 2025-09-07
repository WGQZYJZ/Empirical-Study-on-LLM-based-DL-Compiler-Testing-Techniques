
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 3072)
        self.output_layer = torch.nn.Linear(3072, 768)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(torch.tensor([1]).to('cuda'))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(value)

        return self.output_layer(self.attn(output))

m  = Model()

