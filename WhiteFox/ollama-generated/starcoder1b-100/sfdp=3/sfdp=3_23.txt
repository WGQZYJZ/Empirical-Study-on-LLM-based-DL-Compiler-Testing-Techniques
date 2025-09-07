
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(d_model, d_k)
        self.v  = torch.nn.Linear(d_model, d_v)

    def forward(self, query: Tensor, key: Tensor, value: Tensor):
        kq   = torch.matmul(query, key.transpose(-2, -1))
        vk   = self.v(value)
        softmax_qk  = kq.mul(scale_factor).softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(1, batch_size, seq_len, d_model)
key    = torch.randn(1, batch_size, seq_len, d_k)
value  = torch.randn(1, batch_size, seq_len, d_v)


