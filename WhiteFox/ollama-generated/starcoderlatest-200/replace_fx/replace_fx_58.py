
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.1) # Replace dropout with lowmem_dropout
        v2 = torch.rand_like(v1) # Replace rand_like with rand_like
        return v2


# Initializing the model
m = Model()
gm = gm_tvm.mod.make(m, {"dtype": "float32"}) # Make a graph from the module m and dtype float32 to test gm.lower() functions

# Inputs to the model
x1 = torch.randn(1, 2, 2)
gm = gm_tvm.mod.set_input(gm, x1)
gm = gm_tvm.opt.apply(gm) # Apply all optimization passes in gm
gm_final = gm_tvm.lower(gm) # Lower gm to final target representation (TG) for inference.


# Generate an input tensor to the model
x2  = gm_tvm.mod.set_input(gm_final, x1)

# Apply all optimization passes in gm and gm_final
gm_final = gm_tvm.opt.apply(gm_final)
gm_final = gm_tvm.lower(gm_final)

