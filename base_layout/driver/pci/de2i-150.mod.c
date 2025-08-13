#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

#ifdef CONFIG_UNWINDER_ORC
#include <asm/orc_header.h>
ORC_HEADER;
#endif

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif



static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x47b07b9b, "pci_release_region" },
	{ 0x9d627daf, "pci_enable_device" },
	{ 0x3c9c904a, "pci_read_config_word" },
	{ 0x2b8b7917, "pci_read_config_byte" },
	{ 0x68efcc64, "pci_read_config_dword" },
	{ 0x7104f4f0, "pci_request_region" },
	{ 0x5769e406, "pci_iomap" },
	{ 0xf0fdf6cb, "__stack_chk_fail" },
	{ 0xdd8f2bd9, "__pci_register_driver" },
	{ 0xe3ec2f2b, "alloc_chrdev_region" },
	{ 0x169675e2, "class_create" },
	{ 0x14777360, "cdev_init" },
	{ 0x92649ec3, "device_create" },
	{ 0xaa5419b1, "cdev_add" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0xc5e89969, "pci_unregister_driver" },
	{ 0x288176f5, "class_destroy" },
	{ 0x38655e10, "device_destroy" },
	{ 0x39d2b405, "cdev_del" },
	{ 0x13c49cc2, "_copy_from_user" },
	{ 0x4a453f53, "iowrite32" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0x122c3a7e, "_printk" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0xa78af5f3, "ioread32" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x6b10bee1, "_copy_to_user" },
	{ 0x87a21cb3, "__ubsan_handle_out_of_bounds" },
	{ 0xd6c83743, "pci_iounmap" },
	{ 0xd61983dd, "pci_disable_device" },
	{ 0x6ad2b3e, "module_layout" },
};

MODULE_INFO(depends, "");

MODULE_ALIAS("pci:v00001172d00000004sv*sd*bc*sc*i*");

MODULE_INFO(srcversion, "9C2B7863EAFB5350667DAE3");
