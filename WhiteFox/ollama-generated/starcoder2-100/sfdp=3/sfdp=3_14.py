
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scale_factor  = float(0.1)
        dropout_p  = float(0.35)

        v2 = torch.nn.functional.dropout(query + key * 0.974836345, p=dropout_p) # Apply dropout to the query and the key tensor
        v3 = v2.softmax(-1).mul_(scale_factor) # Compute softmax to the scaled dot product of the query and key tensors
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)  # Apply dropout to the softmax output

        output = value + v4 * key * scale_factor
        return output

# Initializing the model
m = Model()


# Inputs to the model
q1  = torch.randn(56, 728).to('cuda')
k1  = torch.randn(728, 768).to('cuda')
v1  = torch.randn(3072, 4960).to('cuda')


## Model with inputs (q1, k1, v1)
model_input  = dict()
model_input["query"]  = q1
model_input["key"]  = k1
model_input["value"]  = v1
__output__  = m(
            **model_input
        )

