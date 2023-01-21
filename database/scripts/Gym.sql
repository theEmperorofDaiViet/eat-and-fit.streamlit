CREATE TABLE if not exists Gym (
	Day varchar(255) not null,
    Exercise varchar(255) not null,
    Sets varchar(255),
    Reps varchar(255)
);

 /* Query:
 SELECT * FROM eatandfit.Gym WHERE Day = ?;
 */
 
INSERT INTO Gym VALUES  ('lower', '01', '3', '8-10'),
						('lower', '02', '3', '15-20'),
						('lower', '03', '3', '12-15'),
						('lower', '04', '3', '15-20'),
						('lower', '05', '3', '8-10'),
						('lower', '06', '3', '15-20'),
						('upper', '07', '3', '8-10'),
						('upper', '08', '3', '10-12'),
						('upper', '09', '3', '8-10'),
						('upper', '10', '3', '10'),
						('upper', '11', '3', '10-12'),
						('upper', '12', '3', '10');
                        
CREATE TABLE if not exists Exercise (
	Id varchar(255) not null,
    Name varchar(255),
    Link varchar(255),
    Overview text,
    Introductions text,
    primary key (Id)
);

INSERT INTO Exercise VALUES ('01', 'Squats', 'https://www.youtube.com/embed/R2dMsNhN3DE', 'The squat is the king of all exercises, working over 256 muscles in one movement! From bodybuilders to powerlifters to competitive athletes, the squat is a staple compound exercise and should be in every workout plan.;For powerlifters, it is known as one of the “big three” lifts which includes the squat, deadlift, and bench press. For athletes, having an explosive squat is a good indicator for on field/court performance. And for bodybuilders, the squat is a compound exercise that targets nearly every muscle of your lower body and core.;The squat directly targets the muscles of the quads, but also involves the hamstrings, glutes, back, and core as well as muscles of the shoulders and arms to a lesser degree.;Not everyone is built to perform the traditional barbell back squat and it can result in some pain for certain individuals. Over the years, several squatting variations have been developed to help everyone be able to train this critical movement pattern safely.;The emphasis of the squat can be switched from the quads to the hamstrings by your foot placement. Some wear shoes with an elevated heel (or elevate their heels on plates) to focus more on the quads. Others keep a flat foot to put more pressure on the hamstrings.;At the end of the day it is important that you pick a squat variation and foot placement that works best for you and that you can perform safely.'
																						, 'Set up for the exercise by setting the barbell to just below shoulder height and loading the weight you want to use.;Stand under the bar with your feet at about shoulder width apart.;Position the bar so that it is resting on the muscles on the top of your back, not on the back of your neck. The bar should feel comfortable. If it doesn''t, try adding some padding to the bar.;Now take your hands over the back and grip the bar with a wide grip for stability.;You should now bend at the knees and straighten your back in preparation to take the weight off the rack.;Keeping your back straight and eyes up, push up through the legs and take the weight off the rack.;Take a small step back and stabilize yourself.;Keeping your eyes facing forward slowly lower your body down. Don''t lean forward as you come down. Your buttocks should come out and drop straight down.;Squat down until your thighs are parallel with the floor, and then slowly raise your body back up by pushing through your heels.;Do not lock the knees out when you stand up, and then repeat the movement.'),
							('02', 'Leg Press', 'https://www.youtube.com/embed/sEM_zo9w2ss', 'The leg press is a variation of the squat and an exercise used to target the muscles of the leg.;One can utilize the leg press to target both the quads and the hamstring muscle, depending on which portion of the foot they push through.;The leg press is commonly thought of as a machine variation of the barbell back squat. The mechanics are fairly similar, however, the leg press does not completely mimic the movement pattern of the squat. Nor does it work all of the muscle groups that the squat does.;The leg press is best used as an accessory movement to the squat, or as a primary movement in gyms which lack the necessary equipment to train the squat movement pattern.'
																						   , 'Load the machine with the desired weight and take a seat.;Sit down and position your feet on the sled with a shoulder width stance.;Take a deep breath, extend your legs, and unlock the safeties.;Lower the weight under control until the legs are roughly 45 degrees or slightly below.;Drive the weight back to the starting position by extending the knees but don’t forcefully lockout.;Repeat for the desired number of repetitions.'),
							('03', 'Leg Extension', 'https://www.youtube.com/embed/0fl1RRgJ83I', 'The seated leg extension is an isolation exercise and one used to target the muscles of the quads.;This exercise can be particularly hard on the knees. So, for those with prior knee issues, it may be beneficial to stick with other movements, preferably compound, to target your quads.;The leg extension is a great exercise for quad development and may be beneficial to include in your workout routines if your goals are more aesthetics-driven.;The leg extension can be utilized in both leg workouts and full body workouts.'
																							   , 'Select the desired resistance on the weight stack and insert the pin.;Adjust the seat so that the knees are directly in line with the axis of the machine.;Sit down and position your shins behind the pad at the base of the machine.;Take a deep breath and extend your legs as you flex your quadriceps.;As you lock out the knees, exhale to complete the repetition.;Slowly lower your feet back to the starting position and repeat for the desired number of repetitions.'),
							('04', 'Leg Press Calf Raise', 'https://www.youtube.com/embed/RcKQbiL-ZOc', 'The leg press calf raise is a variation of the machine calf raise and an exercise used to build the muscles of the calves.;The calves can be a very stubborn muscle group, so it’s important to target them with plenty of different angles and a with a high training frequency.;This exercise can be incorporated into your leg days or full body days.'
																									  , 'Load the machine with the desired weight and take a seat.;Sit down and position your feet on the sled with a shoulder width stance.;Take a deep breath, extend your legs, but keep the safeties locked (if possible).;Position your feet at the base of the platform and allow the heels to hang off.;Lower the heels by dorsiflexing the ankles until the calves are fully stretched.;Drive the weight back to the starting position by extending the ankles and flexing the calves.;Repeat for the desired number of repetitions.'),
							('05', 'Stiff Leg Deadlift', 'https://www.youtube.com/embed/CkrqLaDGvOA', 'The stiff leg deadlift is a variation of the deadlift and an exercise used primarily to target the muscles of the hamstrings.;The stiff leg deadlift has long been thought of as the “leg” deadlift variation, despite all hip hinge movements primarily targeting the hamstrings. A smart option, to increase training frequency and work on the movement pattern, would be to perform stiff legs on your leg day and another deadlift variation on your back or pull days.;The hip hinge is a crucial movement pattern, so it is important to find a variation that is comfortable for you to perform (if able), and work on it.;The stiff leg deadlift is best utilized during your leg workouts and/or full body workouts.'
																									, 'Position the bar over the top of your shoelaces and assume a hip width stance.;Push your hips back and hinge forward until your torso is nearly parallel with the floor.;Reach down and grasp the bar using a shoulder width, double overhand grip.;Ensure your spine is neutral, shin is vertical, and your hips are roughly the same height as your shoulders.;Drive through the whole foot and focus on pushing the floor away.;Ensure the bar tracks in a straight line as you extend the knees and hips.;Once you have locked out the hips, reverse the movement by pushing the hips back and hinging forward.;Return the bar to the floor, reset, and repeat for the desired number of repetitions.'),
							('06', 'Seated Calf Raise', 'https://www.youtube.com/embed/Yh5TXz99xwY', 'The seated calf raise is a variation of the machine calf raise and an exercise used to isolate the muscles of the calves.;The calves can be a stubborn muscle group for a lot of people, so it’s important to experiment with several different angles when performing calf raises. You may also want to consider training the calves with a high training frequency.;The seated calf raise can be incorporated into your leg workouts and full body workouts.'
																								   , 'Take a seat on the machine and place the balls of your feet on the platform with your toes pointed forward - your heels will naturally hang off. Position the base of quads under the knee pad and allow your hands to rest on top.;Extend your ankles and release the safety bar.;Lower the heels by dorsiflexing the ankles until the calves are fully stretched.;Extend the ankles and exhale as you flex the calves.;Repeat for the assigned number of repetitions.'),
							('07', 'Incline Bench Press', 'https://www.youtube.com/embed/uIzbJX5EVIY', 'The incline bench press is a variation of the bench press and an exercise used to build the muscles of the chest. The shoulders and triceps will be indirectly involved as well.;Utilizing an incline will allow you to better target the upper portion of the chest, a lagging part for a lot of lifters.;You can include incline bench press in your chest workouts, upper body workouts, push workouts, and full body workouts.'
																									 , 'Lie flat on an incline bench and set your hands just outside of shoulder width.;Set your shoulder blades by pinching them together and driving them into the bench.;Take a deep breath and allow your spotter to help you with the lift off in order to maintain tightness through your upper back.;Let the weight settle and ensure your upper back remains tight after lift off.;Inhale and allow the bar to descend slowly by unlocking the elbows.;Lower the bar in a straight line to the base of the sternum (breastbone) and touch the chest.;Push the bar back up in a straight line by pressing yourself into the bench, driving your feet into the floor for leg drive, and extending the elbows.;Repeat for the desired number of repetitions.'),
							('08', 'One Arm Dumbbell Row', 'https://www.youtube.com/embed/YZgVEy6cmaY', 'The one arm dumbbell row is a variation of the dumbbell row and an exercise used to build back muscle and strength.;The back is a muscle group that requires a fair amount of variation. So, experiment with several different angles and hand positions to maximize your back muscle growth.;Rows are a foundational movement pattern and are very important to train for balanced muscle growth and strength. So, experiment until you find a rowing variation that you enjoy and work on it.;The one arm dumbbell row can be performed during your back workouts, upper body workouts, pull workouts, and full body workouts.'
																									  , 'Assume a standing position while holding a dumbbell in one hand with a neutral grip.;Hinge forward until your torso is roughly parallel with the floor (or slightly above) and then begin the movement by driving the elbow behind the body while retracting the shoulder blade.;Pull the dumbbell towards your body until the elbow is at (or just past) the midline and then slowly lower the dumbbell back to the starting position under control.;Repeat for the desired number of repetitions on both sides.'),
							('09', 'Seated Barbell Press', 'https://www.youtube.com/embed/Gxhx7GpRb5g', 'The seated barbell shoulder press is a variation of the overhead press and an exercise used to build shoulder strength and muscle.;Vertical press variations, such as the seated barbell shoulder press, are crucial movement patterns to train and should be incorporated into your workout routines. So, experiment with the variations until you find one that feels comfortable for you to perform and continue to work on it.;The seated barbell shoulder press can be included in your shoulder workouts, push workouts, upper body workouts, and full body workouts.'
																									  , 'Adjust the barbell to just below shoulder height while standing then load the desired weight onto the bar.;Place an adjustable bench beneath the bar in an upright position.;Sit down on the bench and unrack the bar using a pronated grip.;Inhale, brace, tuck the chin, then lower the bar to the top of your chest.;Exhale and press the bar back to lockout.;Repeat for the desired number of repetitions.'),
							('10', 'Pull Ups', 'https://www.youtube.com/embed/5oxviYmdHCY', 'The wide grip pull up is a variation of the pull up and an exercise used to target the upper back muscles such as the latissimus dorsi.;Vertical pulling movements, such as the wide grip pull up, are foundational movements that should be included in your workout routines. So, once you’ve found a variation you like and feels comfortable to you, master it as it will benefit you from a strength and aesthetic standpoint.;The wide grip pull up can be incorporated into back workouts, pull workouts, upper body workouts, or full body workouts.'
																						  , 'Using a pronated grip, grasp the pull bar with a wider than shoulder width grip.;Take a deep breath, squeeze your glutes and brace your abs. Depress the shoulder blades and then drive the elbows straight down to the floor while activating the lats.;Pull your chin towards the bar until the lats are fully contracted, then slowly lower yourself back to the start position and repeat for the assigned number of repetitions.'),
							('11', 'Skullcrushers', 'https://www.youtube.com/embed/K6MSN4hCDM4', 'The EZ bar skullcrusher is a variation of the skullcrusher and an exercise used to strengthen the muscles of the triceps.;The triceps can be trained in many different ways to promote growth and overhead extensions, such as the EZ bar skullcrusher, are an effective way to target the long head of the tricep.;Having bigger and stronger triceps are not only important from an aesthetic standpoint but can also help contribute to better performance on pressing motions such as the bench press.'
																							   , 'Select your desired weight and sit on the edge of a flat bench.;To get into position, lay back and keep the bar close to your chest. Once you are supine, press the weight to lockout.;Lower the weights towards your head by unlocking the elbows and allowing the ez bar to drop toward your forehead or just above.;Once your forearms reach parallel or just below, reverse the movement by extending the elbows while flexing the triceps to lockout the weight.;Repeat for the desired number of repetitions.'),
							('12', 'Dumbbell Bench Press', 'https://www.youtube.com/embed/dGqI0Z5ul4k', 'The dumbbell bench press is a variation of the barbell bench press and an exercise used to build the muscles of the chest.;Often times, the dumbbell bench press is recommended after reaching a certain point of strength on the barbell bench press to avoid pec and shoulder injuries.;Additionally, the dumbbell bench press provides an ego check in the amount of weight used due to the need to maintain shoulder stability throughout the exercise.;The exercise itself can be featured as a main lift in your workouts or an accessory lift to the bench press depending on your goals.'
																									  , 'Pick up the dumbbells off the floor using a neutral grip (palms facing in). Position the ends of the dumbbells in your hip crease, and sit down on the bench.;To get into position, lay back and keep the weights close to your chest. Once you are in position, take a deep breath, and press the dumbbells to lockout at the top.;Slowly lower the dumbbells under control as far as comfortably possible (the handles should be about level with your chest).;Contract the chest and push the dumbbells back up to the starting position.;Repeat for the desired number of repetitions.');