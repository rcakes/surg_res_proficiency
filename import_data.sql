-- Create the database.

-- create database if not exists operative_proficiency;
use operative_proficiency;

-- Create the main data table.
create table cases(
    id int not null auto_increment primary key,
    resident_last_name varchar(50) not null,
    resident_first_name varchar(50) not null,
    pgy int null,
    attending varchar(50) not null,
    case_type varchar(30) null,
    eval_date date null,
    role varchar(2) null,
    pct_res_est int null,
    pct_att_est int null,
    overall_val int null,
    overall_text varchar(50) null,
    category varchar(50) null,
    cpt_code int not null,
    procedure_description varchar(300) null,
    pre_op_pt_info_val int null,
    pre_op_pt_info_text varchar(50) null,
    pre_op_prep_case_dis_val int null,
    pre_op_prep_case_dis_text varchar(50) null,
    pre_op_prep_tech_val int null,
    pre_op_prep_tech_text varchar(50) null,
    lap_ability_assist_val int null,
    lap_ability_assist_text varchar(50) null,
    lap_approp_tissue_val int null,
    lap_approp_tissue_text varchar(50) null,
    lap_dexterity_val int null,
    lap_dexterity_text varchar(50) null,
    lap_depth_percep_val int null,
    lap_depth_percep_text varchar(50) null,
    lap_biman_dexterity_val int null,
    lap_biman_dexterity_text varchar(50) null,
    lap_knot_tie_val int null,
    lap_knot_tie_text varchar(50) null,
    lap_effic_plan_movt_val int null,
    lap_effic_plan_movt_text varchar(50) null,
    lap_indep_op_move_val int null,
    lap_indep_op_move_text varchar(50) null,
    open_ability_assist_val int null,
    open_ability_assist_text varchar(50) null,
    open_approp_tissue_val int null,
    open_approp_tissue_text varchar(50) null,
    open_dexerity_val int null,
    open_dexerity_text varchar(50) null,
    open_biman_dexterity_val int null,
    open_biman_dexterity_text varchar(50) null,
    open_knot_tie_val int null,
    open_knot_tie_text varchar(50) null,
    open_effic_plan_movt_val int null,
    open_effic_plan_movt_text varchar(50) null,
    open_indep_op_move_val int null,
    open_indep_op_move_text varchar(50) null,
    fb_q1_val int null,
    fb_q1_text varchar(50) null,
    fb_q2_val int null,
    fb_q2_text varchar(50) null,
    fb_q3_val int null,
    fb_q3_text varchar(50) null,
    fb_q4_val int null,
    fb_q4_text varchar(50) null,
    fb_q5_val int null,
    fb_q5_text varchar(50)
);


-- Import the data from a file.
load data local infile '/mnt/data/Dropbox/Ruchi and Jonathan Share/Surgical Resident Proficiency/data/cleaned/combined_proficiency_data.csv'
into table cases
fields terminated by '\t'
lines terminated by '\n'
ignore 1 lines
(
    resident_last_name,
    resident_first_name,
    pgy,
    attending,
    case_type,
    eval_date,
    role,
    pct_res_est,
    pct_att_est,
    overall_val,
    overall_text,
    category,
    cpt_code,
    procedure_description,
    pre_op_pt_info_val,
    pre_op_pt_info_text,
    pre_op_prep_case_dis_val,
    pre_op_prep_case_dis_text,
    pre_op_prep_tech_val,
    pre_op_prep_tech_text,
    lap_ability_assist_val,
    lap_ability_assist_text,
    lap_approp_tissue_val,
    lap_approp_tissue_text,
    lap_dexterity_val,
    lap_dexterity_text,
    lap_depth_percep_val,
    lap_depth_percep_text,
    lap_biman_dexterity_val,
    lap_biman_dexterity_text,
    lap_knot_tie_val,
    lap_knot_tie_text,
    lap_effic_plan_movt_val,
    lap_effic_plan_movt_text,
    lap_indep_op_move_val,
    lap_indep_op_move_text,
    open_ability_assist_val,
    open_ability_assist_text,
    open_approp_tissue_val,
    open_approp_tissue_text,
    open_dexerity_val,
    open_dexerity_text,
    open_biman_dexterity_val,
    open_biman_dexterity_text,
    open_knot_tie_val,
    open_knot_tie_text,
    open_effic_plan_movt_val,
    open_effic_plan_movt_text,
    open_indep_op_move_val,
    open_indep_op_move_text,
    fb_q1_val,
    fb_q1_text,
    fb_q2_val,
    fb_q2_text,
    fb_q3_val,
    fb_q3_text,
    fb_q4_val,
    fb_q4_text,
    fb_q5_val,
    fb_q5_text 
);
