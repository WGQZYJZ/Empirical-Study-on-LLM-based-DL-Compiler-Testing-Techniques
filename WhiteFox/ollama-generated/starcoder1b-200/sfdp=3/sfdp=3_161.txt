
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(d_model, d_k)
        self.scale_factor = 10
        self.softmax_qk = torch.nn.functional.softmax(self.qk(q), dim=-1)
        self.dropout_qk = torch.nn.functional.dropout(
            self.softmax_qk, p=dropout_p)

    def forward(self, q, k):
        scaled_qk = q.matmul(k.transpose(-2, -1))
        scaled_qk = scaled_qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
q = torch.randn(batch_size, seq_len, d_model)
k = torch.randn(batch_size, seq_len, d_k)
