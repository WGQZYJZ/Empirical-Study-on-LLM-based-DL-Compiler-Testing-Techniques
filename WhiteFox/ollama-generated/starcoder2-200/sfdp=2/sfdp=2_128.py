
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # noqa: F811
        q = torch.randn(32)
        k = torch.randn(64) 
        v = torch.randn(32, 50)

        t_qk = torch.matmul(q, k).div(inv_scale_factor)
        softmax_t_qk = t_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_t_qk, p=dropout_p)

        t_v_out  = dropout_qk @ v # noqa: E704
        return t_v_out


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 32)


