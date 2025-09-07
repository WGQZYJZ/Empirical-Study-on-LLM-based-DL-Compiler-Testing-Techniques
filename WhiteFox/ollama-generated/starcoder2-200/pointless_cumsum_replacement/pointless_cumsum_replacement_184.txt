
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1=428069357497050752, arg2=- 1094468042273778560):
        v1 = torch.full([arg1, arg2], 1)
        v2 = torch.convert_element_type(v1, 'float')
        v3 = torch.cumsum(v2, dim=1)
        return v3


# Initializing the model
m = Model()
 
 # Inputs to the model
__output__  = m(- 745968043866994304, arg2=- 1094468042273778560)


# This part of this task is optional. If you feel like you've finished the above tasks and have extra time, please generate and share some PyTorch models with public APIs that fulfill the following requirements:

-  A model which contains one call to `torch.ops.prim_ops.isFinite`.
-  A model which contains one call to `torch.ops.aten._index_select_impl_int.default`.
-  A model which contains one call to `torch.ops.aten._empty_affine_.default`.
-  A model which contains one call to `torch.nn.functional.hardtanh()`.
-  A model which contains one call to `torch.nn.utils.clip_grad_value_(v1, v2)` where v1 is a matrix and v2 is a scalar.
