
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(torch.randn((1, )))
 
    def forward(self, qk, key, value, dropout_p=0.2):  # Dropout parameter
        inv_scale_factor = (qk + self.scale).sum(-1) ** -0.5
        softmax_qk  = torch.nn.functional.softmax(qk / scale_factor[-1], dim=-1)
        output = torch.nn.functional.dropout(softmax_qk, p=p) * value # Apply dropout to the softmax output 
        return output


# Initializing the model
m  = Model()
 
