x = Variable(torch.randn(5, 5))
y = Variable(torch.randn(5, 5))
torch.nn.modules.module.register_module_backward_hook(x)