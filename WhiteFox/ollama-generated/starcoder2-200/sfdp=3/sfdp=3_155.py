
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(
            torch.randn(32, 64)
        )
        self.key = torch.nn.Parameter(
            torch.randn(100, 64)
        )
        self.value = torch.nn.Parameter(torch.randn(100, 64))

    def forward(self):
        scaled_qk = torch.matmul(
            self.query, self.key.transpose(-2, -1),
        ) * scale_factor

        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(
            softmax_qk, p=dropout_p, inplace=True
        )

        return dropout_qk.matmul(self.value)

# Initializing the model
m  = Model()
__output__  = m()

