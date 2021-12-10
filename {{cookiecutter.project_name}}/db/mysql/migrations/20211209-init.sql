
-- +migrate Up
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `username` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `avatar` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '头像',
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_email_unique` (`email`),
  UNIQUE KEY `users_phone_unique` (`phone`),
  UNIQUE KEY `users_username_unique` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='用户表';

/******************************************/
/*  密码都是hash后的 12345    */
/******************************************/
INSERT INTO `fastapi`.`users`(`id`, `name`, `email`, `password`, `phone`, `username`, `avatar`, `deleted_at`, `created_at`, `updated_at`) VALUES (1, 'Jack', 'wxy@123.com', '$2b$12$9QqLfn..1PGFMLtoD1xvFOX8IGk/COLBHi8yKLFs.DTsiCyi9QmYq', '17722334455', '旱灾杰克', 'https://avatars.githubusercontent.com/u/33140097', NULL, '2021-12-09 20:29:22', NULL);
INSERT INTO `fastapi`.`users`(`id`, `name`, `email`, `password`, `phone`, `username`, `avatar`, `deleted_at`, `created_at`, `updated_at`) VALUES (2, 'Pony', 'xxxy@123.com', '$2b$12$uV6BtGvW.5e8M6r9YWzkjeAwOq4kPc4U/Ge8wk7Kh0hAtvqG13uBK', '17712346677', '小马宝莉', 'https://avatars.githubusercontent.com/u/27198984', NULL, '2021-12-09 20:35:48', NULL);

-- +migrate Down
DROP TABLE IF EXISTS `users`;
DELETE FROM  users where id =1
DELETE FROM  users where id =2


