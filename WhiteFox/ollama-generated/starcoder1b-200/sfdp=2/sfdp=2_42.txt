
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        vq = self.conv(x1)

        # Scale the dot product by the inverse scale factor: `v/s`
        inv_scale_factor = torch.diag([
            torch.tensor([[0., -1.357649726989743e-06, 0.]], device=x1.device),
            torch.tensor([[-1.357649726989743e-06, 0., 0.],
                          [0., -1.2501592793093954e-06, 0.]]),
            torch.tensor([[-1.2501592793093954e-06, 0., 0.],
                          [0., -1.0807441818114982e-06, 0.]]),
            torch.tensor([[-1.0807441818114982e-06, 0., 0.],
                          [0., -1.0358407750068163e-06, 0.]]),
            torch.tensor([[-1.0358407750068163e-06, 0., 0.],
                          [0., -1.0022193904692587e-06, 0.]]),
            torch.tensor([[-1.0022193904692587e-06, 0., 0.],
                          [0., -1.3581884432040248e-06, 0.]]),
        ])

        # Apply softmax to the scaled dot product: `v/s` -> `softmax(v/s)`
        vq = (vq / inv_scale_factor).softmax(dim=-1)
        vq = torch.nn.functional.dropout(vq, p=dropout_p)

        # Compute the dot product of the dropout output and the value: `d_o * v`
        v  = self.conv(x1)
        output = (v / inv_scale_factor).matmul(vq)
        return output


# Initializing the model
m = Model()


