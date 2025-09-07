import torch  # import pytorch modules for your model
import math
dtype = torch.float32  # float type for tensors that you are creating in the forward function
layout  = torch.strided  # specify layout to use when creating the tensor


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.__device__ = 'cpu'
        self.__layout__ = torch.strided
 
    def forward(self, arg1, arg2): 
        t1  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout) # create a tensor filled with the scalar value of 1
        t2  = convert_element_type(t1, dtype)
        t3  = torch.cumsum(t2, 1)
        return t3


def run_forward():
    m = Model() 
    return m(arg1, arg2), m.train(), m.eval(), m.__device__, m.__layout__


class convert_element_type:
  def __init__(self): pass

  def __call__(tensor, dtype=dtype):
      return tensor.to(dtype)


def torch_cumsum(*args,**kwargs):
    raise NotImplementedError()


