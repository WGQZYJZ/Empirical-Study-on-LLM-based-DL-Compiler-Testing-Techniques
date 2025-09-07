
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ...):
        # ...

    def sink_cat_after_pointwise(model, input_tensor, **kwargs):
        new_input_tensor = torch.cat([input_tensor, ...], dim=-1)  # Concatenate a new tensor along the last dimension
        return model.forward(new_input_tensor)


# Initializing the model
m = Model()

