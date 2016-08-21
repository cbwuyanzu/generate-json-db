CREATE TABLE lamps (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `lamp_name` varchar(32),
    `updatetime` datetime DEFAULT NULL,
	`on_off` tinyint(1),
	`level` int(8),
    `voltage` float,
    `current` float,
    `power` float,
    `power_factor` float,
    `energy` float,
	PRIMARY KEY (`id`)
)   DEFAULT CHARSET=utf8
;