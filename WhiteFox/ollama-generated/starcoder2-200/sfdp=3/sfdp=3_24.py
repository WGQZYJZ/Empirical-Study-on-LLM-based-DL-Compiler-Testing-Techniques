
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        qk  = torch.matmul(x1[:, :, None].expand(-1, -1, x1.size()[-2]),
                           x1[:, :, None].transpose(-2, -1).expand(*x1.shape[:-3], x1.size()[0], *x1.shape[-3:]))
        scaled_qk  = qk / torch.std(qk)
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropouts[0])
        output  = dropout_qk[:, :, None].expand(-1, -1, *x1.shape[:-2], x1.size()[0], qk.size()[-3:-1]).matmul(qk) # A new model!
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn([4, 8])
key  = torch.randn([5, 8])
value  = torch.randn([32, 16])
__output__  = m(torch.stack([query for _ in range(dropouts[0].shape[0])] + [key]))

